provider "google" {
  project = "meu-projeto-dados"
  region  = "us-central1"
}

resource "google_storage_bucket" "lakehouse" {
  name     = "lakehouse-bucket"
  location = "US"
}
