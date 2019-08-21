#!/bin/bash
#Script that takes an URL ($1) and displays all methods
curl -sI $1 | grep Allow: | cut -d ":" -f2 | sed 's/ //'
