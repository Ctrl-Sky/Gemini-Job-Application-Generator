#!/bin/bash

# Get parameters
company_name="$1"
job_title="$2"
month_date="$3"

# Define Path
path="ouputs/$month_date/$company_name-$job_title"

# Check if directory exist, else create it
if [ ! -d "$path" ]; then
    mkdir "$path"