#!/bin/bash

set -e


: ${HOST:=${HOST:='0.0.0.0'}}
: ${PORT:=${PORT:='4200'}}

if [[ $ENV == 'development' ]]; then
	#statements
    ng build;
else
    ng build --prod;
fi

ng serve --host=$HOST --port=$PORT;
