#!/bin/bash
#Script that takes an URL ($1), send a GET request and displays the body of response (-L)
#The response is based on a custom header variable, with 98 value
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
