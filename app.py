from flask import Flask, jsonify, request, blueprints
from models.database import db
from models.user import User
import bcrypt


app = Flask(__name__)
