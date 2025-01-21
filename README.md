# VitalEdge Hobbit

**VitalEdge Hobbit** is a lightweight, Gradio-based internal UI designed for managing and visualizing post-Datalake workflows within the VitalEdge ecosystem. Hobbit enables seamless interaction with advanced analytics workflows such as Retrieval-Augmented Generation (RAG), LangChain orchestrations, Machine Learning (ML) models, and other analytical tools, exclusively through API-based interactions with the Datalake.

---

## **Key Features**

- **RAG Operations**: Manage embeddings, vector similarity searches, and large language model (LLM) interactions.
- **ML Operations**: Facilitate model inference, training workflows, and performance monitoring.
- **Analytics Explorer**: Query and visualize data from the Datalake API in a structured and user-friendly manner.
- **Extensibility**: Designed to support the addition of new workflows, tabs, and sections as needed.
- **API-Driven Architecture**: Ensures clean separation of concerns and a secure interaction with the Datalake and other Mantle components.

---

## **Project Structure**

```plaintext
vitaledge_hobbit/
├── app/
│   ├── components/                # UI components for specific sections
│   │   ├── rag_operations_ui.py   # RAG-related operations
│   │   ├── ml_operations_ui.py    # ML-related operations
│   │   └── datalake_explorer_ui.py# Datalake Explorer operations
│   ├── services/                  # Service layer for external API calls
│   │   ├── datalake_service.py    # Handles Datalake API interactions
│   │   ├── rag_service.py         # Handles RAG operations via APIs
│   │   └── ml_service.py          # Handles ML operations via APIs
│   ├── utils/                     # Reusable utilities
│   │   ├── config.py              # Configuration management
│   │   ├── logger.py              # Centralized logging
│   │   └── request_handler.py     # Common HTTP request handling
│   ├── main.py                    # Application entry point
│   └── templates/                 # Placeholder for future static assets
├── requirements.in                # Base dependencies
├── requirements.txt               # Compiled dependencies
└── README.md                      # Project documentation
```

---

## **Setup and Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repo/vitaledge-hobbit.git
cd vitaledge-hobbit
```

### **2. Create a Virtual Environment**
Using `conda`:
```bash
conda create -n vitaledge-hobbit python=3.11 -y
conda activate vitaledge-hobbit
```

Or using `venv`:
```bash
python -m venv venv
source venv/bin/activate    # On Linux/macOS
venv\Scripts\activate       # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Environment Configuration**
Create a `.env` file in the root directory and define the following variables:
```env
DATALAKE_API_URL=http://127.0.0.1:8005
LOG_LEVEL=INFO
```

### **5. Run the Application**
```bash
python app/main.py
```

Access the application in your browser at [http://127.0.0.1:7860](http://127.0.0.1:7860).

---

## **Features Overview**

### **1. RAG Operations**
- **Embeddings**: Generate embeddings for input text.
- **VectorDB**: Perform vector similarity searches on stored embeddings.
- **LLM**: Generate responses from large language models.
- **RAG Workflow**: Orchestrate end-to-end workflows for RAG tasks.

### **2. ML Operations**
- **Model Inference**: Test pre-trained ML models with real-time inputs.
- **Model Monitoring**: Visualize model performance metrics (future feature).
- **Training**: Initiate and manage ML training workflows (future feature).

### **3. Analytics Explorer**
- **Datalake Explorer**: Query and visualize structured data using APIs.
- **Custom Queries**: Execute analytical queries (future feature).

---

## **Contributing**

Contributions are welcome! Please follow the guidelines below:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push the changes:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## **License**

VitalEdge Hobbit is licensed under the [MIT License](LICENSE).

---

## **Contact**

For issues or inquiries, please reach out to: 
- **Email**: [samseatt@gmail.com](mailto:samseatt@gmail.com)
- **GitHub Issues**: [Issues](https://github.com/samseatt/vitaledge-hobbit/issues)
