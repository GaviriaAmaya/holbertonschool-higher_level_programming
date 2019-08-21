#!/bin/bash
#Script that takes an URL ($1), displays the size of the body response (grep, cut)
curl -sI $1 | grep Content-Length | cut -d " " --f2
