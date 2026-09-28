# ATIVIDADE: braço robótico com grafo de cena.
# Leia ATIVIDADE.md e complete os trechos marcados com TODO.
# ESC fecha. P salva capturas/resultado.png para a entrega.
import argparse

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.object3D import Object3D
from formas import caixa

CINZA = [0.6, 0.62, 0.66]
LARANJA = [0.98, 0.45, 0.2]
AZUL = [0.25, 0.5, 0.95]
VELOCIDADE = 1.5  # radianos por segundo


class Braco(Base):

    def initialize(self):
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.setPosition([0, 1.9, 4.2])
        self.camera.rotateX(-0.2)

        chao = caixa(6, 0.1, 6, [0.8, 0.82, 0.85])
        chao.setPosition([0, -0.05, 0])
        self.scene.add(chao)

        # base: caixa de altura 0.4, apoiada no chão
        self.base = caixa(1.0, 0.4, 1.0, CINZA)
        self.base.setPosition([0, 0.2, 0])
        self.scene.add(self.base)

        self.ombro = Object3D()
        self.ombro.setPosition([0, 0.2, 0])
        self.base.add(self.ombro)
        braco = caixa(0.3, 1.2, 0.3, LARANJA)
        braco.setPosition([0, 0.6, 0])
        self.ombro.add(braco)

        self.cotovelo = Object3D()
        self.cotovelo.setPosition([0, 1.2, 0])
        self.ombro.add(self.cotovelo)
        antebraco = caixa(0.25, 1.0, 0.25, AZUL)
        antebraco.setPosition([0, 0.5, 0])
        self.cotovelo.add(antebraco)

        garra = caixa(0.5, 0.15, 0.5, CINZA)
        garra.setPosition([0, 1.0 + 0.075, 0])
        self.cotovelo.add(garra)

    def update(self):
        angulo = VELOCIDADE * self.deltaTime
        if self.isKeyPressed('a'):
            self.base.rotateY(angulo)
        if self.isKeyPressed('d'):
            self.base.rotateY(-angulo)
        if self.isKeyPressed('w'):
            self.ombro.rotateZ(angulo)
        if self.isKeyPressed('s'):
            self.ombro.rotateZ(-angulo)
        if self.isKeyPressed('i'):
            self.cotovelo.rotateZ(angulo)
        if self.isKeyPressed('k'):
            self.cotovelo.rotateZ(-angulo)
        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Braco(title='Atividade: braço robótico').run(args.frames, args.screenshot)
