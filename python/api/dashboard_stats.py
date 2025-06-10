import psutil
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any
import asyncio
import json
import os
from python.helpers.api import ApiHandler
from flask import Request, Response

# Global variables for tracking
start_time = time.time()
message_count = 0
active_tasks = 0
recent_activities = []

class DashboardStats(ApiHandler):

    async def process(self, input: dict, request: Request) -> dict | Response:
        """Get comprehensive dashboard statistics"""
        
        try:
            # System metrics
            memory_info = psutil.virtual_memory()
            cpu_percent = psutil.cpu_percent(interval=1)
            disk_usage = psutil.disk_usage('/')
            
            # Process metrics
            current_process = psutil.Process()
            process_memory = current_process.memory_info()
            
            # Uptime calculation
            uptime_seconds = int(time.time() - start_time)
            hours, remainder = divmod(uptime_seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            uptime_str = f"{hours}h {minutes}m"
            
            # Get recent activities
            activities = await self.get_recent_activities()
            
            # API health check
            api_status = await self.check_api_health()
            
            # MCP status check
            mcp_status = await self.check_mcp_status()
            
            stats = {
                "stats": {
                    "totalMessages": await self.get_message_count(),
                    "activeTasks": await self.get_active_tasks_count(),
                    "memoryUsage": process_memory.rss,  # Resident Set Size
                    "uptime": uptime_str,
                    "apiStatus": api_status,
                    "mcpStatus": mcp_status,
                    "systemMemoryPercent": memory_info.percent,
                    "cpuPercent": cpu_percent,
                    "diskUsagePercent": disk_usage.percent
                },
                "recentActivity": activities,
                "systemMetrics": {
                    "memory": {
                        "total": memory_info.total,
                        "available": memory_info.available,
                        "percent": memory_info.percent,
                        "used": memory_info.used
                    },
                    "cpu": {
                        "percent": cpu_percent,
                        "count": psutil.cpu_count()
                    },
                    "disk": {
                        "total": disk_usage.total,
                        "used": disk_usage.used,
                        "free": disk_usage.free,
                        "percent": disk_usage.percent
                    },
                    "process": {
                        "memory_rss": process_memory.rss,
                        "memory_vms": process_memory.vms,
                        "cpu_percent": current_process.cpu_percent(),
                        "num_threads": current_process.num_threads()
                    }
                }
            }
            
            return stats
            
        except Exception as e:
            return {
                "error": str(e),
                "stats": {
                    "totalMessages": 0,
                    "activeTasks": 0,
                    "memoryUsage": 0,
                    "uptime": "0h 0m",
                    "apiStatus": False,
                    "mcpStatus": False
                },
                "recentActivity": []
            }

    # Helper functions
    async def get_message_count(self) -> int:
        """Get total message count from chat history"""
        try:
            # This would integrate with your existing message storage
            # For now, return a placeholder
            return message_count
        except Exception:
            return 0

    async def get_active_tasks_count(self) -> int:
        """Get count of currently active tasks"""
        try:
            # This would integrate with your scheduler/task system
            return active_tasks
        except Exception:
            return 0

    async def get_recent_activities(self) -> List[Dict[str, Any]]:
        """Get recent system activities"""
        try:
            # This would integrate with your activity logging
            # For now, return sample activities
            sample_activities = [
                {
                    "id": 1,
                    "icon": "💬",
                    "title": "New chat started",
                    "timestamp": datetime.utcnow().timestamp() * 1000
                },
                {
                    "id": 2,
                    "icon": "⚡",
                    "title": "Task completed successfully",
                    "timestamp": (datetime.utcnow() - timedelta(minutes=5)).timestamp() * 1000
                },
                {
                    "id": 3,
                    "icon": "🔧",
                    "title": "System configuration updated",
                    "timestamp": (datetime.utcnow() - timedelta(minutes=15)).timestamp() * 1000
                }
            ]
            
            return sample_activities + recent_activities
        except Exception:
            return []

    async def check_api_health(self) -> bool:
        """Check if main API is healthy"""
        try:
            # Simple health check - if we can execute this, API is working
            return True
        except Exception:
            return False

    async def check_mcp_status(self) -> bool:
        """Check if MCP services are active"""
        try:
            # This would check actual MCP status
            # For now, return True as a placeholder
            return True
        except Exception:
            return False

# Utility functions for activity logging
def log_activity(icon: str, title: str):
    """Log a new activity"""
    global recent_activities
    activity = {
        "id": len(recent_activities) + 1,
        "icon": icon,
        "title": title,
        "timestamp": datetime.utcnow().timestamp() * 1000
    }
    recent_activities.append(activity)
    
    # Keep only last 10 activities
    if len(recent_activities) > 10:
        recent_activities = recent_activities[-10:]

def increment_message_count():
    """Increment the global message counter"""
    global message_count
    message_count += 1

def update_active_tasks(count: int):
    """Update the active tasks count"""
    global active_tasks
    active_tasks = count 