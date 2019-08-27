#!/bin/bash
#Script that takes an URL ($1), send a GET request and displays the body of response (-L)
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X "POST" "$1"
