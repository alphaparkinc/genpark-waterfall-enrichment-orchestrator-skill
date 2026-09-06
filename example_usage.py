import json
from client import WaterfallEnrichmentOrchestrator

def main():
    orchestrator = WaterfallEnrichmentOrchestrator()
    sample_query = {
        "first_name": "Elena",
        "last_name": "Vance",
        "title": "VP of Engineering",
        "domain": "acmesystems.io"
    }
    result = orchestrator.enrich_prospect(sample_query)
    print("Waterfall Enrichment Result:")
    print(json.dumps(result, indent=2))
    assert result["firmographics"]["company_name"] == "Acme Systems Inc."
    assert result["target_contact"]["email_status"] == "deliverable"
    print("Waterfall enrichment verification complete: PASS")

if __name__ == "__main__":
    main()
