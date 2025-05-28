{
    "name": "Stage Management",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Gestion Simplifiée des Stages en Entreprise",
    "description": """
        Module de gestion des stages académiques permettant de suivre:
        - Les étudiants
        - Les entreprises partenaires
        - Les tuteurs académiques et professionnels
        - Les conventions de stage
        - Les rapports de stage
    """,
    "author": "Votre Nom",
    "website": "https://www.example.com",
    "depends": ["base", "mail", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_views.xml",
        "views/company_views.xml",
        "views/tutor_views.xml",
        "views/internship_views.xml",
        "views/report_views.xml",
        "report/internship_agreement_template.xml",
        "report/internship_agreement_report.xml",
        "views/menu_views.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
