from flaskr.core.base.repository import BaseRepository
from flaskr.domains.orders.models import Order


class OrderRepository(BaseRepository[Order]):
    model = Order
