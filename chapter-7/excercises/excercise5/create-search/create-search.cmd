@echo off

rem Set values for your Search service, find it from the Azure portal
rem set url=https://ai102srch1124418192.search.windows.net // example url
rem set admin_key=HOBSHDa20W9999gSej9y8UAz99999999SeCdxFo2  // example admin key

set url=https://[YOUR_SEARCH_URL].search.windows.net
set admin_key=YOUR_ADMIN_KEY 

echo -----
echo Creating the data source...
call curl -X POST %url%/datasources?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: %admin_key%" -d @data_source.json

echo -----
echo Creating the skillset...
call curl -X PUT %url%/skillsets/hotels-custom-skillset?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: %admin_key%" -d @skillset.json

echo -----
echo Creating the index...
call curl -X PUT %url%/indexes/hotels-custom-index?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: %admin_key%" -d @index.json

rem wait
timeout /t 3 /nobreak

echo -----
echo Creating the indexer...
call curl -X PUT %url%/indexers/hotels-custom-indexer?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: %admin_key%" -d @indexer.json
