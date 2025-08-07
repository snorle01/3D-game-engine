#version 330 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 uv_vert;
layout (location = 2) in float light_level;

out vec2 uv_pos;
out float light;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

void main() {
    gl_Position = m_proj * m_view * m_model * vec4(position, 1.0);
    uv_pos = uv_vert;
    light = light_level;
}