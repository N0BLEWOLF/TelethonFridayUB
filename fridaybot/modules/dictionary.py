#    Copyright (C) @chsaiujwal 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
try:
  from nltk.corpus import wordnet 
except:
  import nltk
  nltk.download('wordnet')
  from nltk.corpus import wordnet 
from uniborg.util import edit_or_reply, friday_on_cmd, sudo_cmd	

from fridaybot import CMD_HELP	


@friday.on(friday_on_cmd("meaning (.*)"))	
@friday.on(sudo_cmd("meaning (.*)", allow_sudo=True))	
async def _(event):	
    omg = await edit_or_reply(event, "Finding Meaning.....")	
    if event.fwd_from:	
      return	
    input_str = event.pattern_match.group(1)
    try:
      try:
        syns = wordnet.synsets(input_str)
      except:
        import nltk
        nltk.download('wordnet')
        from nltk.corpus import wordnet 
        syns = wordnet.synsets(input_str)
      Kk = 0
      for X in syns:
        Kk +=1
      pop = 0
      kok = 1
    
      messi = ""
      for pop in range(Kk):
        messi += str(syns[pop].definition())+";  \n"
        pop +=1
      mil = syns[0].examples()
      if [] == mil:
        mil = input_str+"..."
        await omg.edit(f"<b> meaning of {input_str} is:-</b>\n{messi}.\n\n<b>Example:- </b>\n{mil}",parse_mode="HTML")	
      else:
        milo = ""
        for lm in mil:
          milo += lm+"; \n"
        await omg.edit(f"<b> meaning of {input_str} is:-</b>\n{messi}\n\n<b>Examples:- </b>\n{milo}",parse_mode="HTML")
    except:
      await omg.edit(f"<b> Meaning Not Found</b>", parse_mode="HTML")



CMD_HELP.update(
    {
    "dictionary": "**Dictionary**\
\n\n**Syntax : **`.meaning <Word>`\
\n**Usage :** Gives meaning of the word."
    }
)
