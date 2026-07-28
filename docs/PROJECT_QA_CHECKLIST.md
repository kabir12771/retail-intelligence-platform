\# Project QA Checklist  

\# Retail Intelligence Platform



\## 1. Purpose



This checklist is used to review the Retail Intelligence Platform before final portfolio publishing, interview presentation, and GitHub release.



The QA review covers:



\- Repository structure

\- Python ETL pipeline

\- SQL Server warehouse

\- Validation framework

\- Audit and logging

\- Power BI dashboards

\- Documentation

\- GitHub readiness

\- Portfolio presentation quality



\---



\## 2. Repository QA



| Check | Status |

|---|---|

| Git repository initialized | Completed |

| GitHub remote connected | Completed |

| Main branch pushed | Completed |

| `.gitignore` added | Completed |

| `.env` excluded from GitHub | Completed |

| `.env.example` added | Completed |

| Virtual environment excluded | Completed |

| Log files excluded | Completed |

| Generated operational files excluded | Completed |

| GitHub Actions workflow added | Completed |

| Working tree clean after commits | Completed |



\---



\## 3. Folder Structure QA



| Folder | Purpose | Status |

|---|---|---|

| `audit/` | Audit logging logic | Completed |

| `config/` | Pipeline and DB configuration | Completed |

| `docs/` | Project documentation | Completed |

| `extract/` | Excel extraction logic | Completed |

| `load/` | SQL load logic | Completed |

| `validate/` | Validation framework | Completed |

| `utils/` | Helper utilities | Completed |

| `tests/` | Test scripts | Completed |

| `powerbi/` | Power BI report and DAX files | Completed |

| `screenshots/` | Dashboard screenshots | Completed |

| `sql/demo\_data/` | Demo data expansion scripts | Completed |



\---



\## 4. Python ETL QA



| Check | Status |

|---|---|

| Main pipeline entry point exists | Completed |

| Excel source files can be read | Completed |

| File type detection implemented | Completed |

| Schema validation implemented | Completed |

| Data quality checks implemented | Completed |

| SQL staging load implemented | Completed |

| DW procedure execution implemented | Completed |

| Post-load validation implemented | Completed |

| Error report generation implemented | Completed |

| Run summary report generation implemented | Completed |

| File movement implemented | Completed |

| CLI arguments implemented | Completed |

| Professional logging implemented | Completed |



\---



\## 5. SQL Server QA



| Check | Status |

|---|---|

| SQL Server database created | Completed |

| Staging schema available | Completed |

| Data warehouse schema available | Completed |

| Mart schema available | Completed |

| Audit schema available | Completed |

| Dimension tables created | Completed |

| Fact tables created | Completed |

| Mart views created | Completed |

| Forecast fact table expanded for dashboard demo | Completed |

| Stock optimization fact table expanded for dashboard demo | Completed |



\---



\## 6. Data Validation QA



| Validation Area | Status |

|---|---|

| Required column validation | Completed |

| Required value validation | Completed |

| Date validation | Completed |

| Numeric validation | Completed |

| Duplicate business key validation | Completed |

| Business rule validation | Completed |

| Post-load row count validation | Completed |

| Audit validation | Completed |

| Mart view validation | Completed |



\---



\## 7. Power BI QA



| Check | Status |

|---|---|

| Power BI PBIX file created | Completed |

| Power BI theme added | Completed |

| Executive Overview page created | Completed |

| Sales Performance page created | Completed |

| Forecast Accuracy page created | Completed |

| Stock Optimization page created | Completed |

| Screenshots exported | Completed |

| Screenshots added to README | Completed |

| DAX measure files created | Completed |

| Standalone mart-view model documented | Completed |

| Auto relationships issue documented | Completed |

| Power BI user guide created | Completed |



\---



\## 8. Power BI Model Rule QA



For this portfolio version:



```text

One dashboard page = one mart view

One mart view = one standalone reporting table

No relationships between mart views

Do not mix fields from different mart tables in the same visual

