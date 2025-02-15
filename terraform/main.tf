resource "azurerm_resource_group" "rg_rag" {
  name     = var.resource_group_name
  location = var.resource_group_location
}

resource "azurerm_search_service" "search" {
  name                = var.search_service_name
  resource_group_name = azurerm_resource_group.rg_rag.name
  location            = azurerm_resource_group.rg_rag.location
  sku                 = var.sku
  replica_count       = var.replica_count
  partition_count     = var.partition_count
}

##### OpenAI models #####

resource "azurerm_cognitive_account" "cognitive_account" {
  name                = var.cognitive_account_name
  location            = azurerm_resource_group.rg_rag.location
  resource_group_name = azurerm_resource_group.rg_rag.name
  kind                = "OpenAI"
  sku_name            = var.sku
}

resource "azurerm_cognitive_deployment" "text-embedding" {
  name                 = "text-embedding"
  cognitive_account_id = azurerm_cognitive_account.cognitive_account.id
  model {
    format  = "OpenAI"
    name    = "text-embedding-ada-002"
    version = "2"
  }

  scale {
    type = var.scale
  }
}

resource "azurerm_cognitive_deployment" "gpt3" {
  name                 = "gpt-4o-mini"
  cognitive_account_id = azurerm_cognitive_account.cognitive_account.id
  model {
    format  = "OpenAI"
    name    = "gpt-35-turbo"
    version = "1106"
  }

  scale {
    type = var.scale
  }
}


##### Form Recognizer #####

resource "azurerm_cognitive_account" "document_intelligence" {
  name                = "ocr"
  location            = azurerm_resource_group.rg_rag.location
  resource_group_name = azurerm_resource_group.rg_rag.name
  kind                = "FormRecognizer"
  sku_name            = var.sku
}
