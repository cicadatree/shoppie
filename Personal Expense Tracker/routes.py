from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from models import User, Transaction, Category
from forms import RegistrationForm, LoginForm, TransactionForm, CategoryForm

# Define routes for user registration, login, logout, transaction management, category management, etc.
