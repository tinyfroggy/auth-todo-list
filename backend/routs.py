from flask import jsonify, request
from models import Users, Tasks


def register_routes(app, db):
    @app.route("/", methods=["POST", "GET"])
    @app.route("/register", methods=["POST", "GET"])
    def register_func():
        if request.method == "POST":
            data = request.get_json()
            first_name = data.get("firstName")
            last_name = data.get("lastName")
            email = data.get("email")
            password = data.get("password")
            gender = data.get("gender")

            if (
                not first_name
                or not last_name
                or not email
                or not password
                or not gender
            ):
                return jsonify(
                    {"status": "error", "message": "All fields should be filled."}
                ), 400

            existing_user = Users.query.filter_by(email=email).first()
            if existing_user:
                return jsonify(
                    {"status": "error", "message": "Email is already in use."}
                ), 400

            user = Users(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password_hash=password,
                gender=gender,
            )
            db.session.add(user)
            db.session.commit()

            return {"status": "success", "message": "User registered successfully"}, 200

        return jsonify(
            {"status": "error", "message": "Use POST method to register."}
        ), 400

    @app.route("/login", methods=["POST", "GET"])
    def login_func():
        if request.method == "POST":
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return (
                    jsonify(
                        {"status": "error", "message": "All fields should be filled."}
                    ),
                    400,
                )

            existing_user = Users.query.filter_by(email=email).first()
            if not existing_user:
                return (
                    jsonify(
                        {"status": "error", "message": "The email is not defined."}
                    ),
                    400,
                )

            if existing_user.password_hash != password:
                return (
                    jsonify(
                        {"status": "error", "message": "The password is incorrect."}
                    ),
                    400,
                )

            return (
                {"status": "success", "message": "User logged in successfully"},
                200,
            )

    @app.route("/tasks", methods=["POST", "GET"])
    def tasks_func():
        if request.method == "POST":
            data = request.get_json()
            title = data.get("title")
            description = data.get("description")

            if not title or not description:
                return jsonify(
                    {"status": "error", "message": "All fields should be filled."}
                ), 400

            task = Tasks(
                task_title=title,
                task_description=description,
            )
            db.session.add(task)
            db.session.commit()

            return jsonify(
                {"status": "success", "message": "Task added successfully"}
            ), 200

        tasks = Tasks.query.all()
        return jsonify(
            {"status": "success", "tasks": [task.to_json() for task in tasks]}
        ), 200

    @app.route("/tasks/<int:task_id>", methods=["GET"])
    def get_task(task_id):
        task = Tasks.query.get_or_404(task_id)
        return jsonify(
            {
                "status": "success",
                "message": "Task found successfully",
                "task": task.to_json(),
            }
        ), 200

    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def delete_task(task_id):
        task = Tasks.query.get_or_404(task_id)

        try:
            db.session.delete(task)
            db.session.commit()
            return jsonify(
                {"status": "success", "message": "Task deleted successfully"}
            ), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def update_task(task_id):
        task = Tasks.query.get_or_404(task_id)

        try:
            data = request.get_json()
            task.task_title = data.get("task_title", task.task_title)
            task.task_description = data.get("task_description", task.task_description)

            db.session.commit()

            return jsonify(
                {"status": "success", "message": "Task updated successfully"}
            ), 200

        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    
    @app.route("/tasks/<int:task_id>", methods=["PATCH"])
    def complete_task(task_id):
        task = Tasks.query.get_or_404(task_id)

        try:
            data = request.get_json()
            task.task_status = data.get("task_status", task.task_status)
            
            db.session.commit()

            return jsonify({
                "status": "success",
                "message": "Task status updated successfully",
                "task": task.to_json() 
            }), 200

        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

