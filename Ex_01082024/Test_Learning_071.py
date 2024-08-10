## Request Module > Module > Package or library which contains functionsn
# which you can use easily in your code
# math,os,allure,pytest,csv these are the modules which we import.

# to make the http - method
# request module is used to make the http - method
# GET ,POST,PUT,DELETE,PATCH,HEAD,OPTIONS
# URL,Authentication,Cookies,Verification with pytest

# GET request - Booking Id
# While making Request Client >>>> Server
# URL - https://restful-booker.herokuapp.com/booking
# AUth > NA
# Payload - NA
# Headers - NA
# Method - GET
# Query param - NA
# PAth PAram - 1 - Required

# Response what we need to verify
# 1. Status code
# 2. Response body >> verify>> assert , keys values
# 3. Response header
# 4. Response cookies
# 5. Response time
# 6. JSON Schema , XML Schema

import allure
import pytest
import requests
# -s which help you to print the details
