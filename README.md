# AI-Powered IoT Analytics & Automation Platform with GenAI Agents

This project is a real-time, end-to-end IoT intelligence platform that integrates sensor-driven data collection with cloud-native ETL, deep learning, and GenAI-powered automation.
The architecture is built by ` Abhishek Amar ` on AWS and Databricks, combining traditional data engineering with modern LLM-based agents for predictive insights, anomaly detection, 
and autonomous decision-making.

# IoT Sensor Layer
  Physical IoT devices collect real-time environmental, motion, or equipment data.  
  Data is sent via MQTT to AWS IoT Core.
# AWS IoT Rules Engine routes incoming data to: 
    Amazon SQS for message buffering 
    Amazon Lambda for light preprocessing, filtering, and event-driven transformation 
    Data is also forwarded to Databricks Delta Lake for persistent storage

# Databricks is used to build modular ETL pipelines:
  Extract: From SQS, IoT device logs, or Delta Lake
  Transform: Data cleaning, validation, enrichment (feature engineering, timestamp normalization)
  Load: To Delta Tables, PostgreSQL, or MongoDB for downstream processing
  Pipelines support both batch and streaming data

# Data Science & Deep Learning
  -----------------------------------------------------------------------------------------------------------------------
  Data Ingestion : Using Bricks
  ------------------------------------------------------------------------------------------------------------------------
  Model Evaluation  --> Deploy --> Monitor --> Retraining :- Using MLOPS
  ------------------------------------------------------------------------------------------------------------------------
  Data Ingestion --> preprocessing --> EDA --> Model creation --->Model Evaluation  --> Deploy --> Monitor --> Retraining 
  ------------------------------------------------------------------------------------------------------------------------
  Predictive modeling (e.g., failure prediction, sensor drift)  
  Models built using PyTorch and TensorFlow  
  Automated anomaly detection using LSTM/GRU time series models  
  ML models are deployed with MLflow on Databricks
  
# LLM Agents (LangChain + LangGraph) + Langsmith (for logs)
  LangChain agents respond to anomalies and recommend remediation steps
  Integrated with SQS and Lambda for real-time triggering
  Agents communicate using event-driven LangGraph workflows

# Prompt Engineering
Custom system and user prompts guide agents in:
  Interpreting sensor patterns  
  Generating alerts or maintenance tasks  
  Summarizing ETL reports

# LLM Fine-Tuning
  Fine-tuned OpenAI or Hugging Face LLMs on:
  Sensor logs
  Maintenance manuals
  Support tickets
  
# MCP & MLOps Layer
  Model Control Plane (MCP) handles:
  Experiment tracking
  Versioning and registry of fine-tuned LLMs
  Canary deployments and rollback
  CI/CD for models using Databricks Repos or GitHub Actions
  Monitoring via MLflow 
