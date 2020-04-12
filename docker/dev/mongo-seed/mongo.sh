#!/bin/sh

until nc -z mongodb 27017
do
    echo "Waiting for Mongo to start..."
    sleep 0.5
done

eval $*