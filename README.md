# SwedQ Interview Task (vehicles)

## Architecture

The solution is simply a django application running behind an Angular app.

![architectural sketch](documentation/architecture.png?raw=true "architectural sketch")

## Analysis
The frontend is built in Angular, simply it's a table that displays the result of api call.
The api call contains 2 optional arguments, that filters on the status of the vehicle and the customer name.

If the `RANDOM_VEHICLE_STATUS` environment variable is set to `'True'`, the randomization mechanizm will write random status to each vehicle every 10 seconds.

## Cloud deployment 
The solution is docker-friendly, so it's prefarred to be deployed to the cloud on a docker-orchestration service (Kubernates cluster or AWS ECS).

The database used in this solution is `SQLite3`.

`AWS ElasticCache` could be used as a replacement for `redis`.

## Deployment steps
### Local environment
You will need to install `docker` and `docker-compose`.


Just run the following command then navigate to `http://localhost:4200` in your browser.

```
$ docker-compose up -d 
```

### Deployment to the cloud
As mentioned, you can deploy it to `AWS ECS` and the `taskdef` should be very similar to what is written in the `docker-compose.yml` file.

## Environment variables

### Backend
|   Variable	            |   Description	                                    |
|:-------------:            |-------------------------------------              |
|DJANGO_SETTINGS_MODULE     |Django settings module name.                       |
|CELERY_BROKER_URL          |`redis` url for celery to use as a message broker. |
|CELERY_RESULT_BACKEND      |`redis` url for celery to use as result backend (defaults to same value as `CELERY_BROKER_URL`)|
|ENV                        |Runtime environment tag, defaults to `development`.|
|RANDOM_VEHICLE_STATUS      |Whether the randomization mechanizm should work, defaults to `True`|
|HOST                       |Host ip for the app to bind, defaults to `0.0.0.0`.|
|PORT                       |Port for the app to bind, defaults to `5000`.      |


### Frontend
|   Variable	            |   Description	                                    |
|:-------------:            |-------------------------------------              |
|ENV                        |Runtime environment tag, defaults to `development`.|
|HOST                       |Host ip for the app to bind, defaults to `0.0.0.0`.|
|PORT                       |Port for the app to bind, defaults to `4200`.      |