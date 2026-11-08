const express = require("express");
const controller = require("../controllers/roomController");
const auth = require("../middleware/authMiddleware");

const router = express.Router();

router.use(auth);
router.get("/", controller.list);
router.post("/", controller.create);
router.put("/:id", controller.update);
router.delete("/:id", controller.remove);

module.exports = router;
