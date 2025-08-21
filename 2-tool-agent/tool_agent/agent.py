#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2025-08-21 09:25

"""Agent."""

from datetime import datetime
from typing import Dict
from google.adk.agents import Agent


__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"


def get_current_time() -> Dict:
    return {"current_time": datetime.now().strftime("%Y-%m-%d T%H:%M:%S %p")}


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    instruction="""
    You're an AI assistant who has access to following tools to
    take help and answer user's queries.
    - get_current_time
    """,
    description="An AI Assistant to answer users' queries.",
    tools=[
        get_current_time,
    ],
)
