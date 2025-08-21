#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2025-08-21 09:25

"""Agent."""

from google.adk.agents import Agent


__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"


root_agent = Agent(
    name="basic_agent",  # No issues, better to align with package name?
    model="gemini-2.0-flash",
    instruction="You're a greeter agent who ask the user their name greet them by name.",
    description="An agent who greets user by their name",
)
