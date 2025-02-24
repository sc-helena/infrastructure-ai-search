variable "resource_group_location" {
  type        = string
  description = "Location for all resources."
  default     = "swedencentral"
}

variable "resource_group_name" {
  type        = string
  description = "Name of the ressource group."
  default     = "ai-search-cv-rg"
}

variable "search_service_name" {
  type        = string
  description = "Name of the search service."
  default     = "ai-search"
}

variable "cognitive_account_name" {
  type        = string
  description = "Name of the cognitive account."
  default     = "cognitive_account"
}

variable "sku_name" {
  description = "The pricing tier of the search service you want to create (for example, basic or standard)."
  default     = "S0"
  type        = string
}

variable "scale" {
  description = "The pricing tier of the search service you want to create (for example, basic or standard)."
  default     = "Standard"
  type        = string
}

variable "replica_count" {
  type        = number
  description = "Replicas distribute search workloads across the service. You need at least two replicas to support high availability of query workloads (not applicable to the free tier)."
  default     = 1
  validation {
    condition     = var.replica_count >= 1 && var.replica_count <= 12
    error_message = "The replica_count must be between 1 and 12."
  }
}

variable "partition_count" {
  type        = number
  description = "Partitions allow for scaling of document count as well as faster indexing by sharding your index over multiple search units."
  default     = 1
  validation {
    condition     = contains([1, 2, 3, 4, 6, 12], var.partition_count)
    error_message = "The partition_count must be one of the following values: 1, 2, 3, 4, 6, 12."
  }
}
