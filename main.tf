resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.resource_group_location
}

resource "random_string" "azurerm_search_service_name" {
  length  = 25
  upper   = false
  numeric = false
  special = false
}

resource "azurerm_search_service" "search" {
  name                = random_string.azurerm_search_service_name.result
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = var.sku
  replica_count       = var.replica_count
  partition_count     = var.partition_count
}

resource "azurerm_resource_group" "rg_rag" {
  name     = "rg_rag"
  location = "Sweden Central"
}

resource "azurerm_cognitive_account" "cognitive_account" {
  name                = "cognitive_account"
  location            = azurerm_resource_group.rg_rag.location
  resource_group_name = azurerm_resource_group.rg_rag.name
  kind                = "OpenAI"
  sku_name            = "S0"
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
    type = "Standard"
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
    type = "Standard"
  }
}
