#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
__author__ = 'Mohamad-Husari'

import datetime
import time


class Equipo:
    def __init__(self, id_club, nombre):
        self.id_club = id_club
        self.nombre = nombre

    def __str__(self):
        return "%s - %s" % (self.id_club, self.nombre)


class Partido:
    def __init__(self, id_partido, dae_mach, temporada, jornada, local,
                 visitante, goles_local, goles_visitante, fecha):
        self.idPartido = id_partido
        self.dae_mach = dae_mach
        self.temporada = temporada
        #self.division = division
        self.jornada = jornada
        self.local = local
        self.visitante = visitante
        self.golesLocal = goles_local
        self.golesVisitante = goles_visitante
        self.fecha = fecha
        self.timestamp = int(time.mktime(
            datetime.datetime.strptime(fecha, "%d/%m/%Y").timetuple()))

    def __str__(self):
        return "%s::%s::%s::%s::%s::%s::%s::%s::%s::%s" \
               % (self.idPartido, self.dae_mach, self.temporada, self.jornada,
                  self.local, self.visitante, self.golesLocal,
                  self.golesVisitante, self.fecha, self.timestamp)
