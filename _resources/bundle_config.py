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
        "job_id": 870724760777759,
        "creator_user_name": "vipada.siripatanadilok@adastragrp.com",
        "run_as_user_name": "vipada.siripatanadilok@adastragrp.com",
        "run_as_owner": True,
        "settings": {
            "name": "Task_Test_dbdemos_notebook_1",
            "email_notifications": {
                "no_alert_for_skipped_runs": False
            },
            "webhook_notifications": {},
            "timeout_seconds": 0,
            "max_concurrent_runs": 1,
            "tasks": [
                {
                    "task_key": "Task_Test_dbdemos_notebook_1",
                    "notebook_task": {
                        "notebook_path": "/Users/vipada.siripatanadilok@adastragrp.com/dbDemos/Test_dbdemos_notebook_1",
                        "source": "WORKSPACE"
                    },
                    "existing_cluster_id": "0307-065426-vfnmzpu9",
                    "timeout_seconds": 0,
                    "email_notifications": {}
                }
            ],
            "format": "MULTI_TASK"
        },
        "created_time": 1678250654220
    }
}
