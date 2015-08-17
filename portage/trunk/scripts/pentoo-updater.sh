#!/bin/sh
printf "Pentoo overlay is out of date in layman, fixing...\n"
layman -d pentoo && layman -a pentoo
printf "Please re-run pentoo-updater.\n"
