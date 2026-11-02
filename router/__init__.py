"""Routing package: decides which agent should handle a query."""

from router.query_router import QueryRouter, RouteResult

__all__ = ["QueryRouter", "RouteResult"]
