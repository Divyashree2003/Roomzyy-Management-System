import ManagementPage from "../components/ManagementPage";

const fields = [
  { name: "roomNumber", label: "Room Number", required: true },
  { name: "floor", label: "Floor", required: true },
  { name: "capacity", label: "Capacity", type: "number", required: true },
  { name: "occupiedBeds", label: "Occupied Beds", type: "number", defaultValue: 0 },
  { name: "rentPerBed", label: "Rent Per Bed", type: "number", required: true },
  {
    name: "status",
    label: "Occupancy Status",
    type: "select",
    options: ["Available", "Occupied", "Maintenance"],
    defaultValue: "Available",
  },
];

const columns = [
  { key: "roomNumber", label: "Room" },
  { key: "floor", label: "Floor" },
  { key: "capacity", label: "Capacity" },
  { key: "occupiedBeds", label: "Occupied" },
  { key: "status", label: "Status" },
];

function RoomManagement(props) {
  return (
    <ManagementPage
      {...props}
      title="Room Management"
      subtitle="Maintain room list, capacity, rent, and occupancy status."
      resource="rooms"
      fields={fields}
      columns={columns}
    />
  );
}

export default RoomManagement;
