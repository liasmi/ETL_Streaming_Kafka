# My Project

This is a Python project demonstrating the use of various features and best practices.

## Overview

This project extracts data from an API and, using Airflow, streams the data into a Kafka broker. The streaming data is then processed by a Spark job and the results are stored in Cassandra, all managed through Docker Compose.

## Features

- **API Data Extraction**: Fetch data from an external API.
- **Airflow Orchestration**: Use Airflow to schedule and manage data workflows.
- **Kafka Integration**: Stream data into Kafka for real-time processing.
- **Spark Processing**: Utilize Apache Spark to process streaming data.
- **Cassandra Storage**: Store the processed results in a Cassandra database.
- **Docker Compose**: Manage all services using Docker Compose for containerization.

## Project Structure

- `dags/`: Contains Airflow DAGs for scheduling data extraction and processing tasks.
- `scripts/`: Python scripts for data extraction and processing.
- `spark/`: Spark job definitions for processing the streaming data.
- `config/`: Configuration files for Kafka, Spark, and Cassandra.
- `docker-compose.yml`: Docker Compose file to set up and run all necessary services.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/liasmi/ETL_Streaming_Kafka.git
    cd ETL_Streaming_Kafka
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Start services using Docker Compose:**

    Ensure Docker is running, then execute:

    ```sh
    docker-compose up -d
    ```

    This will start all the necessary services including Airflow, Kafka, Spark, and Cassandra.

5. **Access the services:**

    - **Airflow UI:** [http://localhost:8080](http://localhost:8080)
    - **Kafka Broker:** [http://localhost:9092](http://localhost:9092)
    - **Spark UI:** [http://localhost:4040](http://localhost:4040)
    - **Cassandra:** Running on default port `9042`

## Usage

- **Airflow UI:** Access the Airflow web interface at `http://localhost:8080` to manage and monitor your workflows.
- **Kafka Broker:** The Kafka broker will receive and stream the data.
- **Spark Jobs:** Spark jobs will process the streamed data from Kafka.
- **Cassandra Database:** The processed data will be stored in Cassandra.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
