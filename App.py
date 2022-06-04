#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[2]:


from flask import Flask


# In[3]:


from flask import render_template, request


# In[4]:


app = Flask(__name__)


# In[5]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        return (render_template("index.html", result = "temp"))
    else: 
        return (render_template("index.html", result = "waiting..."))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




