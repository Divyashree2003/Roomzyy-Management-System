const mongoose = require("mongoose");

const roomSchema = new mongoose.Schema(
  {
    roomNumber: { type: String, required: true, unique: true, trim: true },
    floor: { type: String, required: true, trim: true },
    capacity: { type: Number, required: true, min: 1 },
    occupiedBeds: { type: Number, default: 0, min: 0 },
    rentPerBed: { type: Number, required: true, min: 0 },
    status: {
      type: String,
      enum: ["Available", "Occupied", "Maintenance"],
      default: "Available",
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Room", roomSchema);
