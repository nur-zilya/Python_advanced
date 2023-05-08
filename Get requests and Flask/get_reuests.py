from typing import List, Optional
import datetime

from flask import Flask, request

app = Flask(__name__)

@app.route("/search/", methods=["GET"])
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids or any(x <= 0 for x in cell_tower_ids):
        return "You must specify at least one valid cell_tower_id", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")

    for prefix in phone_prefixes:
        if not prefix[:-1].isdigit() or not prefix.endswith("*"):
            return "Phone prefix must consist of digits and end with '*'", 400
        elif len(prefix[:-1]) > 10:
            return "Phone prefix is too long. Must be not greater than 10", 400

    protocols: List[str] = request.args.getlist("protocol")

    protocols_list = ["2G", "3G", "4G"]

    if any(protocol not in protocols_list for protocol in protocols):
        return "Protocol type is not correct. Must be one of: 2G, 3G, 4G", 400

    signal_level: Optional[float] = request.args.get("signal_level", type=float)

    date_from: Optional[str] = request.args.get("date_from")

    date_to: Optional[str] = request.args.get("date_to")

    if date_from and date_to:
        try:
            date_from_obj = datetime.datetime.strptime(date_from, "%Y%m%d")
            date_to_obj = datetime.datetime.strptime(date_to, "%Y%m%d")
        except ValueError:
            return "Invalid date format. Must be YYYYMMDD", 400

        if date_from_obj > date_to_obj:
            return "Date from must be less than or equal to date to", 400

        if date_to_obj > datetime.datetime.now():
            return "Date to cannot be in the future", 400

    return f"Search for {cell_tower_ids} call towers. Search criteria: phone_prefixes={phone_prefixes}, protocols={protocols}, signal_level={signal_level}, date_from={date_from}, date_to={date_to}"


if __name__ = "__main__":
    app.run(debug=True)