# Products Specification

This is an executable specification file for the PRODUCTS feature.

## A random product contains all the necessary fields
tags: product

* Product has all fields.

## The total number of products in backend is matching the one from db

* Total number of products is correct.

## Keyword search works as expected

* Searching for a word through products
    | Word       | Status |
    |----------- |--------|
    | python     | true   |
    | asfasf     | false  |
    | javaSCRIPT | true   |
    | 412414     | false  |