from engine.libs.glad cimport *
from engine.texture cimport Texture


cdef class Surface(Texture):
    cdef:
        GLuint fbo
