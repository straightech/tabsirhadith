#/bin/bash

# set -a
# . .env
# set +a
#
# . "$(dirname "$0")/globals.sh"
#
# json_path=src/lib/collections.json
# routes_path=src/lib/enteries.js
#
# if [ ! -f "$json_path" ]; then
#   log blue "Fetching json response from server"
#   curl -o $json_path ${API_URL}/collections
#   log green "Fetched json response from server"
# fi
#
# if [ ! -f "$routes_path" ]; then
#   log blue "Generating routes"
#   cd src/lib
#   bun genEnteries.js
#   cd ../..
# fi
#
# log green "JSON DB exists!"
# echo ''
