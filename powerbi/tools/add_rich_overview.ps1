param(
    [Parameter(Mandatory = $true)]
    [string]$PbixPath
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$sourcePage = 'b2550d813cc76af1b705'
$newPage = 'f0e1d2c3b4a596877869'
$backupPath = [IO.Path]::Combine(
    [IO.Path]::GetDirectoryName($PbixPath),
    [IO.Path]::GetFileNameWithoutExtension($PbixPath) + '.before_rich_overview.pbix'
)
$tempPath = [IO.Path]::Combine(
    [IO.Path]::GetDirectoryName($PbixPath),
    [IO.Path]::GetFileNameWithoutExtension($PbixPath) + '.rich_overview.tmp.pbix'
)

if (-not (Test-Path -LiteralPath $backupPath)) {
    Copy-Item -LiteralPath $PbixPath -Destination $backupPath
}
Copy-Item -LiteralPath $PbixPath -Destination $tempPath -Force

$archive = [IO.Compression.ZipFile]::Open($tempPath, [IO.Compression.ZipArchiveMode]::Update)
try {
    if ($null -ne $archive.GetEntry("Report/definition/pages/$newPage/page.json")) {
        throw "The target page '$newPage' already exists."
    }

    $sourcePrefix = "Report/definition/pages/$sourcePage/"
    $sourceEntries = @($archive.Entries | Where-Object { $_.FullName.StartsWith($sourcePrefix) })

    foreach ($entry in $sourceEntries) {
        $reader = [IO.StreamReader]::new($entry.Open())
        try {
            $content = $reader.ReadToEnd()
        }
        finally {
            $reader.Dispose()
        }

        $newEntryName = $entry.FullName.Replace($sourcePrefix, "Report/definition/pages/$newPage/")

        if ($entry.FullName.EndsWith('/page.json')) {
            $page = $content | ConvertFrom-Json
            $page.name = $newPage
            $page.displayName = 'Retail Intelligence 360 Overview'
            $content = $page | ConvertTo-Json -Depth 100 -Compress
        }
        elseif ($entry.FullName.EndsWith('/visuals/6063b15cb859c400b13a/visual.json')) {
            $content = $content.Replace(
                'Retail Intelligence Platform - Executive Overview',
                'Retail Intelligence 360 Overview'
            )
        }
        elseif ($entry.FullName.EndsWith('/visuals/056d4403a877aa8ab9ac/visual.json')) {
            $content = $content.Replace('Stock Optimization', 'Executive KPI')
            $content = $content.Replace('season', 'region')
        }
        elseif ($entry.FullName.EndsWith('/visuals/163282adecb7da0ff696/visual.json')) {
            $content = $content.Replace('Forecast Accuracy', 'Executive KPI')
            $content = $content.Replace('channel_name', 'city')
        }
        elseif ($entry.FullName.EndsWith('/visuals/76ab31cd747e60d1e8a0/visual.json')) {
            $content = $content.Replace('Forecast Accuracy', 'Executive KPI')
            $content = $content.Replace('Forecast Accuracy %', 'Executive Inventory Markup %')
        }
        elseif ($entry.FullName.EndsWith('/visuals/a402b12ad027403c6e5d/visual.json')) {
            $content = $content.Replace('Stock Optimization', 'Executive KPI')
            $content = $content.Replace('Average Inventory Health Score', 'Executive Sales to Inventory Ratio')
            $content = $content.Replace('Avg. Inventory Health Score', 'Sales / Inventory')
        }
        elseif ($entry.FullName.EndsWith('/visuals/350f979f8689359dc03e/visual.json')) {
            $content = $content.Replace('Transfers', 'Executive KPI')
            $content = $content.Replace('Transfer Completion %', 'Executive Performance Status')
            $content = $content.Replace('Forecast Accuracy %', 'Performance Status')
        }
        elseif ($entry.FullName.EndsWith('/visuals/e968607b2242e2108fd2/visual.json')) {
            $content = $content.Replace('Forecast Accuracy', 'Executive KPI')
            $content = $content.Replace('product_code', 'location_code')
            $content = $content.Replace('product_name', 'location_name')
            $content = $content.Replace('Top Products by Sales', 'Executive Performance Detail')
        }

        $newEntry = $archive.CreateEntry($newEntryName, [IO.Compression.CompressionLevel]::Optimal)
        $writer = [IO.StreamWriter]::new($newEntry.Open(), [Text.UTF8Encoding]::new($false))
        try {
            $writer.Write($content)
        }
        finally {
            $writer.Dispose()
        }
    }

    $pagesEntry = $archive.GetEntry('Report/definition/pages/pages.json')
    $reader = [IO.StreamReader]::new($pagesEntry.Open())
    try {
        $pages = $reader.ReadToEnd() | ConvertFrom-Json
    }
    finally {
        $reader.Dispose()
    }
    $pagesEntry.Delete()
    $pages.pageOrder = @($newPage) + @($pages.pageOrder)
    $pages.activePageName = $newPage
    $newPagesEntry = $archive.CreateEntry(
        'Report/definition/pages/pages.json',
        [IO.Compression.CompressionLevel]::Optimal
    )
    $writer = [IO.StreamWriter]::new($newPagesEntry.Open(), [Text.UTF8Encoding]::new($false))
    try {
        $writer.Write(($pages | ConvertTo-Json -Depth 100 -Compress))
    }
    finally {
        $writer.Dispose()
    }

    $securityBindings = $archive.GetEntry('SecurityBindings')
    if ($null -ne $securityBindings) {
        $securityBindings.Delete()
    }
}
finally {
    $archive.Dispose()
}

Move-Item -LiteralPath $tempPath -Destination $PbixPath -Force

[PSCustomObject]@{
    Pbix = $PbixPath
    Backup = $backupPath
    NewPage = $newPage
    DisplayName = 'Retail Intelligence 360 Overview'
}
