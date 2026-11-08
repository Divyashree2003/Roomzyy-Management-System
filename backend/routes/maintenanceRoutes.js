const express = require("express");
const controller = require("../controllers/maintenanceController");
const auth = require("../middleware/authMiddleware");

const router = express.Router();

router.use(auth);
router.get("/", controller.list);
router.post("/", controller.create);
router.put("/:id", controller.update);
router.patch("/:id/resolve", controller.resolve);
router.delete("/:id", controller.remove);

module.exports = router;
