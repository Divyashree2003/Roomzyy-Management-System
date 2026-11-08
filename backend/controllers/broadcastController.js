const Broadcast = require("../models/Broadcast");
const MessageLog = require("../models/MessageLog");
const controller = require("./crudController")(Broadcast);

const baseCreate = controller.create;

controller.create = async (req, res) => {
  try {
    const broadcast = await Broadcast.create(req.body);
    await MessageLog.create({
      channel: "Broadcast",
      recipient: broadcast.audience,
      message: `${broadcast.title}: ${broadcast.message}`,
      status: "Sent",
    });

    res.status(201).json(broadcast);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

controller.baseCreate = baseCreate;

module.exports = controller;
