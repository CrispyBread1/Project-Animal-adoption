from flask import render_template, Blueprint, redirect, request

from repositories import animal_repository
from repositories import shelter_repository

adoption_blueprint = Blueprint("animals", __name__)

