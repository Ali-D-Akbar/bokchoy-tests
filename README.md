# bokchoy-tests

Follow these steps to run the tests:
1. run `docker-compose build` to make an image from dockerfile.
2. run `docker-compose up -d` to start the containers in detached mode.
3. run `make geckodriver` to install geckodriver locally.
4. `cd demo/app/tests` and run `python test_polls.py` to run the bokchoy acceptance tests.

TODO: Configure to run the tests inside the docker container by running `docker exec -t -i demo.app /bin/bash`
