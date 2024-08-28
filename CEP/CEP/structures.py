project_structures = {
    "api": {
        "src": [
            "main.py",
            "utils.py",
            "config.py",
            "routes.py",
            "models.py",
            "__init__.py"
        ],
        "tests": [
            "test_main.py",
            "test_routes.py",
            "test_models.py"
        ],
        "docs": [
            "README.md",
            "API_DOCS.md"
        ],
        "config": [
            "config.yaml",
            "logging.conf"
        ],
        "empty": [".keep"]  # Añadido para los directorios vacíos
    },
    "react": {
        "src": [
            "App.js",
            "index.js",
            "components/ComponentA.js",
            "components/ComponentB.js",
            "hooks/useCustomHook.js",
            "services/apiService.js",
            "contexts/ContextProvider.js"
        ],
        "public": [
            "index.html",
            "favicon.ico",
            "manifest.json"
        ],
        "tests": [
            "App.test.js",
            "components/ComponentA.test.js"
        ],
        "docs": [
            "README.md",
            "CHANGELOG.md",
            "CONTRIBUTING.md"
        ],
        "styles": [
            "App.css",
            "index.css",
            "components/ComponentA.css"
        ],
        "empty": [".keep"]  # Añadido para los directorios vacíos
    },
    "data_science": {
        "src": [
            "data_preprocessing.py",
            "model.py",
            "training.py",
            "evaluation.py",
            "utils.py",
            "__init__.py"
        ],
        "notebooks": [
            "exploratory_analysis.ipynb",
            "model_training.ipynb",
            "results_analysis.ipynb"
        ],
        "data": [
            "raw_data/.keep",  # Añadido archivo .keep
            "processed_data/.keep"  # Añadido archivo .keep
        ],
        "docs": [
            "README.md",
            "DATA_DICTIONARY.md",
            "PROJECT_PLAN.md"
        ],
        "scripts": [
            "data_cleaning_script.py",
            "feature_engineering_script.py"
        ]
    },
    "ml": {
        "src": [
            "train.py",
            "predict.py",
            "evaluate.py",
            "model.py",
            "utils.py",
            "__init__.py"
        ],
        "notebooks": [
            "exploratory_data_analysis.ipynb",
            "model_training.ipynb",
            "hyperparameter_tuning.ipynb"
        ],
        "data": [
            "raw/.keep",  # Añadido archivo .keep
            "processed/.keep"  # Añadido archivo .keep
        ],
        "docs": [
            "README.md",
            "MODEL_DOCUMENTATION.md",
            "DATA_DESCRIPTION.md"
        ],
        "config": [
            "config.yaml",
            "logging.yaml"
        ]
    },
    "backend": {
        "src": [
            "app.py",
            "models.py",
            "routes.py",
            "services.py",
            "utils.py",
            "__init__.py"
        ],
        "tests": [
            "test_app.py",
            "test_routes.py",
            "test_services.py"
        ],
        "docs": [
            "README.md",
            "API_REFERENCE.md",
            "ARCHITECTURE.md"
        ],
        "config": [
            "config.env",
            "logging.config"
        ],
        "scripts": [
            "database_setup.py",
            "data_migration.py"
        ],
        "empty": [".keep"]  
    },
    "frontend": {
        "src": [
            "index.html",
            "main.js",
            "app.js",
            "components/Navbar.js",
            "components/Footer.js",
            "styles.css"
        ],
        "public": [
            "favicon.ico",
            "manifest.json"
        ],
        "tests": [
            "app.test.js",
            "components/Navbar.test.js"
        ],
        "docs": [
            "README.md",
            "CHANGELOG.md",
            "CONTRIBUTING.md"
        ],
        "styles": [
            "main.css",
            "components/Navbar.css",
            "components/Footer.css"
        ],
        "empty": [".keep"]  
    }
}
