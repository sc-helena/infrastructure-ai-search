# Azure AI Document Intelligence and Search Integration

This project deploys Azure AI services (Document Intelligence, AI Search, OpenAI) using Terraform and provides a Python script to create search indexes and upload documents.

## Prerequisites

- **Azure Account** with active subscription
- **Azure CLI** installed and logged in (`az login`)
- **Terraform** installed ([download](https://www.terraform.io/downloads))
- **Python 3.9+** installed
- **Git** (for cloning repository)

## Project Structure

```
.
├── terraform/               # Infrastructure as Code (IaC) definitions
│   ├── main.tf              # Main Terraform configuration
│   ├── variables.tf         # Variable declarations
│   ├── outputs.tf           # Output values
│   └── providers.tf         # Setup Azure as Provider
│
└── src/                     # Python application code
    ├── assets/              # Documents to be processed
    ├── main_index.py        # Main script for index creation/document upload
    ├── config.py            # Contains configuration variables
    ├── embedder/            # Module contains scripts for the embedding process using OpenAI embedders
    ├── indexing             # Module contains scripts for creating an index and uploading documents
    ├── langChainSplitter    # Module contains scripts for splitting texts into chunks
    └── requirements.txt     # Python dependencies
```

## Getting Started

### 1. Terraform Deployment (Infrastructure Setup)

```bash
cd terraform

# Initialize Terraform
terraform init

# Review execution plan
terraform plan

# Apply configuration
terraform apply
```

**Note:** 
- Review/modify `variables.tf` before applying
- Costs may incur for Azure resources

### 2. Application Setup

#### Create and Activate Virtual Environment
```bash
cd src
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Configure Environment
Create `.env` file with values from Terraform outputs. Use .env.example to check what variables are required.
```

#### Run Document Processing
```bash
python main_index.py
```

## Development Setup

1. Clone repository:
   ```bash
   git clone <repository-url>
   ```

2. Set up virtual environment (as shown above)

3. Install development requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Place documents to process in `/src/assets` folder (supports PDF, DOCX, PNG, JPG)

## Important Notes

- 💡 **Cost Warning**: Azure resources may incur costs. Destroy when not in use:
  ```bash
  terraform destroy
  ```
- 📁 Supported document formats: PDF, Word, PowerPoint, Images
- 🔐 Keep credentials secure - never commit `.env` files
- ⚠️ Run Terraform deployment before using Python scripts
