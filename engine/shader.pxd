from engine.libs.glad cimport *
from engine.libs.cglm cimport *

cdef struct s_Shader:
    GLuint ID, vs_ID, fs_ID

cdef void shader_create(s_Shader *self, const char *vs_path, const char *fs_path)

cdef void shader_destroy(const s_Shader *self)

cdef void shader_use(const s_Shader *self)

cdef void shader_set_int_array(const s_Shader *self, const char *name, GLsizei count, const GLint *values)

cdef void shader_set_mat4(const s_Shader *self, const char *name, const mat4 mat)


# cdef class Shader:
#     cdef s_Shader shader

