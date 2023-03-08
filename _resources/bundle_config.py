# Databricks notebook source
{
    "name": "motest",
    "category": "Test",
    "title": "motest_dbdemos.",
    "description": "Mo test dbdemos 1",
    "bundle": True,
    "tags": [],
    "notebooks": [
        {
            "path": "Test_dbdemos_notebook_1.ipynb",
            "pre_run": True,
            "publish_on_website": True,
            "add_cluster_setup_cell": True,
            "title":  "Mo test 1",
            "description": "Mo test dbdemos 1",
            "parameters": {}
        }
    ],
  "init_job": {
    "settings": {
        "name": "demos_mo_init_{{CURRENT_USER_NAME}}",
        "email_notifications": {
            "no_alert_for_skipped_runs": False
        },
        "timeout_seconds": 0,
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "task_key": "init_data",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/_resources/Test_dbdemos_notebook_1",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            }
        ]
    }
  }
}
