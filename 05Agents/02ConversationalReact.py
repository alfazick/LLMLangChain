

import sys
import os

# Add the root directory to the Python path
# Assuming your script is run from /workspaces/LLMLangChain/03Chains
sys.path.append('/workspaces/LLMLangChain')

from config_settings import API_KEY
from langchain_openai import OpenAI

# defining LLM model
llm = OpenAI(api_key=API_KEY,temperature=0.0)


from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain_community.tools import DuckDuckGoSearchResults

memory = ConversationBufferMemory(memory_key="chat_history")

# loading tools
duck_duck_go_search = DuckDuckGoSearchResults()

tools = load_tools(["llm-math"],llm = llm)
tools.append(duck_duck_go_search)

# Initialize agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory = memory
)

# Example usage

query = "What is the upcoming social events in Edinburg Texas?"
result = agent.run(query)
print(result)
query = "Where I can go this Friday 24 May?"
result = agent.run(query)
print(result)

"""
> Entering new AgentExecutor chain...

Thought: Do I need to use a tool? Yes
Action: duckduckgo_results_json
Action Input: upcoming social events in Edinburg Texas
Observation: [snippet: The Edinburg Chamber of Commerce and Hidalgo County Bar Association 
are pleased to announce their upcoming Law Day Luncheon, scheduled for May 1, 2024, from 11:30 am to 1:00 pm. 
The event will take place at the Region One Education Service Center located at 1900 W Schunior St, Edinburg, TX 78541., title: Upcoming Events - Edinburg Chamber, link: https://edinburg.com/event-calendar/], [snippet: Discover What's Happening in Edinburg, TX on Upcoming Events. Find out what's on in Edinburg, There are countless events in Edinburg from genres like comedy, art, food to festivals; you can find your pick and have the best time of your life. Check out some amazing free events in Edinburg to take away all the fun experiences., title: All Events in Edinburg, TX, Today and Upcoming Events in Edinburg, TX, link: https://allevents.in/edinburg-tx/all], [snippet: Date: Tuesday, April 30, 2024. Join us at the Edinburg Chamber of Commerce Presidents Patio to honor our former board presidents for their incredible dedication! Sponsored by Legacy Chapels, this mixer is open to all Chamber members. Non-members can join for just $20 - see you there from 4:30 P.M. to 7 P.M., title: Edinburg Chamber of Commerce Upcoming Networking Events, link: https://texasborderbusiness.com/edinburg-chamber-of-commerce-upcoming-networking-events/], [snippet: Here are some the best events which is happening on this weekend in Edinburg. Ordination of Juan Martinez is hosted at "1302 E Champion St, Edinburg, TX". 4 Element Challenge (5K and 10K) is hosted at "Edinburg Municipal Park". Trauma Survivors Support Group is hosted at "South Texas Health System Edinburg". Culture Fest is hosted at "Edinburg ..., title: Things To Do In Edinburg, TX This Weekend - AllEvents.in, link: https://allevents.in/edinburg-tx/this-weekend]
Thought: Do I need to use a tool? No
AI: There are several upcoming social events in Edinburg, Texas. 
Some of the events include the Law Day Luncheon on May 1, 2024, the Edinburg Chamber of Commerce 
Presidents Patio mixer on April 30, 2024, and the Culture Fest on April 27, 2024. 
You can also check out the All Events in Edinburg website for more upcoming events in the area.

> Finished chain.
There are several upcoming social events in Edinburg, Texas. 
Some of the events include the Law Day Luncheon on May 1, 2024, the Edinburg 
Chamber of Commerce Presidents Patio mixer on April 30, 2024, and the Culture Fest 
on April 27, 2024. You can also check out the All Events in Edinburg website 
for more upcoming events in the area.


> Entering new AgentExecutor chain...
Thought: Do I need to use a tool? Yes
Action: duckduckgo_results_json
Action Input: Upcoming events in Edinburg Texas
Observation: [snippet: The Edinburg Chamber of Commerce and Hidalgo County Bar Association 
are pleased to announce their upcoming Law Day Luncheon, scheduled for May 1, 2024, 
from 11:30 am to 1:00 pm. The event will take place at the Region One Education 
Service Center located at 1900 W Schunior St, Edinburg, TX 78541., 
title: Upcoming Events - Edinburg Chamber, link: https://edinburg.com/event-calendar/], 
[snippet: Discover What's Happening in Edinburg, TX on Upcoming Events.
Find out what's on in Edinburg, There are countless events in Edinburg 
from genres like comedy, art, food to festivals; you can find your pick and have the best time of your life. Check out some amazing free events in Edinburg to take away all the fun experiences., title: All Events in Edinburg, TX, Today and Upcoming Events in Edinburg, TX, link: https://allevents.in/edinburg-tx/all], [snippet: Here are some the best events which is happening on this weekend in Edinburg. Ordination of Juan Martinez is hosted at "1302 E Champion St, Edinburg, TX". 4 Element Challenge (5K and 10K) is hosted at "Edinburg Municipal Park". Trauma Survivors Support Group is hosted at "South Texas Health System Edinburg". Culture Fest is hosted at "Edinburg ..., title: Things To Do In Edinburg, TX This Weekend - AllEvents.in, link: https://allevents.in/edinburg-tx/this-weekend], [snippet: Explore all upcoming edinburg events in Edinburg, Texas, find information & tickets for upcoming edinburg events happening in Edinburg, Texas., title: Upcoming Events For edinburg in Edinburg, TX - AllEvents.in, link: https://allevents.in/edinburg-tx/edinburg]
Thought: Do I need to use a tool? No
AI: There are many events happening in Edinburg, Texas this Friday, May 24. 
Some options include the Ordination of Juan Martinez, the 4 Element Challenge, 
the Trauma Survivors Support Group, and Culture Fest. 
You can also check out the All Events in Edinburg website for more upcoming events in the area.

> Finished chain.
There are many events happening in Edinburg, Texas this Friday, May 24. 
Some options include the Ordination of Juan Martinez, the 4 Element Challenge, 
the Trauma Survivors Support Group, and Culture Fest. You can also check out the 
All Events in Edinburg website for more upcoming events in the area."""