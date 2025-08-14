"""Inventory management with subrent support."""
from dataclasses import dataclass, field
from typing import Dict, List, Iterable


@dataclass
class InventoryItem:
    """Represents one unit of equipment stored in the inventory."""
    name: str
    quantity: int
    condition: str
    subrent_cost: float


@dataclass
class SubRentRequest:
    """Request to rent additional equipment from external suppliers."""
    item_name: str
    quantity: int
    status: str = "pending"


@dataclass
class Inventory:
    """A simple inventory store of equipment."""
    items: Dict[str, InventoryItem] = field(default_factory=dict)

    def load_equipment(self, equipment: Iterable[Dict[str, object]]) -> None:
        """Load a list of equipment definitions into the inventory.

        Each element in ``equipment`` should be a mapping containing the keys
        ``name``, ``quantity``, ``condition`` and ``subrent_cost``.
        """
        for entry in equipment:
            item = InventoryItem(
                name=str(entry["name"]),
                quantity=int(entry["quantity"]),
                condition=str(entry["condition"]),
                subrent_cost=float(entry["subrent_cost"]),
            )
            self.items[item.name] = item

    def calculate_requirements(self, required: Dict[str, int]) -> List[SubRentRequest]:
        """Compare required volumes with available stock.

        For every equipment name in ``required`` the method ensures there is
        enough quantity in the inventory.  If the remaining stock is
        insufficient a :class:`SubRentRequest` is created for the missing
        amount.  Returns a list of all created requests.
        """
        requests: List[SubRentRequest] = []
        for name, needed in required.items():
            item = self.items.get(name)
            available = item.quantity if item else 0
            if available >= needed:
                if item:
                    item.quantity -= needed
                continue

            missing = needed - available
            requests.append(SubRentRequest(item_name=name, quantity=missing))
            if item:
                item.quantity = 0
            else:
                self.items[name] = InventoryItem(name=name, quantity=0, condition="unknown", subrent_cost=0.0)
        return requests


def generate_report(requests: Iterable[SubRentRequest], path: str = "subrent_report.html") -> str:
    """Create a very small HTML report of subrent requests.

    The returned value is the path to the generated report file.
    """
    rows = [
        f"<tr><td>{r.item_name}</td><td>{r.quantity}</td><td>{r.status}</td></tr>"
        for r in requests
    ]
    body = "\n".join(rows)
    html = (
        "<html><head><meta charset='utf-8'><title>Subrent Report</title></head>"
        "<body><table border='1'>"
        "<tr><th>Item</th><th>Quantity</th><th>Status</th></tr>"
        f"{body}</table></body></html>"
    )
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path
