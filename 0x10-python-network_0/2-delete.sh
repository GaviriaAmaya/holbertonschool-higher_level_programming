#!/bin/bash
#Script that takes an URL ($1), send a DELETE request and displays the body of response (-L)
curl -sX "DELETE" "$1"
